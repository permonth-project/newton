// import React from 'react';
import Navbar from '../components/Navbar';
import LineChart from '../components/dashboard/Linechart';
import { Box } from "@mui/material";
import axios from "axios";
import { useState, useEffect } from 'react';
import Select, { components, PlaceholderProps } from 'react-select';


export default function Dashboard() {
    const [APIData, setAPIData] = useState(null);
    const [modelName, setModelName] = useState(null);
    const [modelOptions, setModelOptions] = useState(null);
    const [capacity, setCapacity] = useState(null);
    const [capacityOptions, setCapacityOptions] = useState(null);
    const [color, setColor] = useState(null);
    const [colorOptions, setColorOptions] = useState(null);;
    const [userSelectedOption, setUserSelectedOption] = useState(null);
    const [priceData, setPriceData] = useState([]);
    const [priceAvg, setPriceAvg] = useState(null);
    const [priceMin, setPriceMin] = useState(null);
    const [priceMax, setPriceMax] = useState(null);
    const [notFoundMSG, setNotFoundMSG] = useState(null);

    // Format options in array format into an array of objects with "value" and "label" keys fro the dropdown
    function formatOptions(options) {
        return (options.map(opt => (
            {
                value: opt,
                label: opt
            }
        )))
    }

    // Get model options at page load
    useEffect(() => {
        axios.get(`http://newton.permonth.tech/api/get-products`).then((response) => {
            setAPIData(response.data);
            setModelOptions(formatOptions(Array.from(new Set(response.data.map((d) => (d.model_name)))).reverse()))
        })
    }, [modelName, capacity, color]);
    if (!APIData) return null;

    // Handle model option change events
    const handleModelChange = (obj) => {
        var filteredArray = APIData.filter(function (d) {
            if (!obj) {
                return
            } else {
                return d.model_name === obj.value;
            }
        });
        var filteredCapacityArray = Array.from(new Set(filteredArray.map(({ id, model_name, color, capacity }) => (capacity))))
        setCapacityOptions(formatOptions(filteredCapacityArray))

        var filteredColorArray = Array.from(new Set(filteredArray.map(({ id, model_name, color, capacity }) => (color))))
        if (filteredArray.length > 0 && filteredColorArray.length === 1 && !filteredColorArray[0]) {
            setColorOptions([{ value: null, label: 'Default Color' }])
        } else {
            setColorOptions(formatOptions(filteredColorArray))
        }
        setModelName(obj)
        setCapacity(null)
        setColor(null)
    }

    // Handle capacity option change events
    const handleCapacityChange = (obj) => {
        setCapacity(obj)
    }

    // Handle color option change events
    const handleColorChange = (obj) => {
        setColor(obj)
    }

    // Handle product selection events when the select button is clicked
    const handleProductSelect = (obj) => {
        var opt = APIData.filter(function (d) {
            if (!obj) {
                return
            } else {
                return d.model_name === modelName.value &&
                    (capacity ? (d.capacity === capacity.value) : 1) &&
                    (color ? (d.color === color.value) : 1)
            }
        })
        var productId = opt.map(d => (
            d.id
        ))

        getProductData(productId)
    };
    // 417, 408, 350, 347

    const handleManualProductSelect = (selectedOption) => {
        var opt = APIData.filter(function (d) {
            if (!selectedOption) {
                return
            } else {
                return d.model_name === selectedOption.model_name &&
                    (capacity ? (d.capacity === selectedOption.capacity) : 1) &&
                    (color ? (d.color === selectedOption.color) : 1)
            }
        })
        console.log('man', opt)
        var productId = opt[0].id
        getProductData(productId)
    }

    function getProductData(productId) {
        var opt = {
            modelName: modelName.value,
            capacity: (capacity ? capacity.value : null),
            color: (color ? color.value : null)
        }
        setUserSelectedOption(opt)
        if (priceData == undefined) {
            setPriceData([{ id: 0, data: [{ x: '', y: 0 }] }])
        }
        axios.get(`http://newton.permonth.tech/api/get-avg-multiple?product_id=${productId}`).then((response) => {
            if (!response.data) {
                setNotFoundMSG(`${opt.modelName} ${opt.capacity ? opt.capacity : ''} ${opt.color ? opt.color : ''} is not found.`)
                setColor(null)
                setCapacity(null)
                setPriceAvg(null)
                setPriceMin(null)
                setPriceMax(null)
                return
            } else {
                setNotFoundMSG('')
            }
            const priceAvgArray = response.data.map((d) => (d.price_avg))
            const priceResultArray = [{
                id: response.data[0].group_id,
                data: response.data.map((d) => (
                    {
                        x: d.result_date_onlydate,
                        y: d.price_avg
                    }
                ))
            }]
            console.log('opt', userSelectedOption)
            setPriceData(priceResultArray)
            setPriceAvg(priceAvgArray.reduce((a, b) => a + b, 0) / priceAvgArray.length)
            setPriceMin(Math.min(...priceAvgArray))
            setPriceMax(Math.max(...priceAvgArray))
        })
    }

    return (
        <>
            <Navbar />
            <div className="max-w-[1240px] mx-auto text-black">
                <div style={{ display: 'flex', gap: '15px' }}>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                        <div style={{ borderBottom: 'solid 1px gray', padding: '30px 0' }}>
                            <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                                <span>Average price of</span>
                                <Select
                                    placeholder={'Model'}
                                    styles={{ menu: ({ ...css }) => ({ ...css, width: 'max-content' }) }}
                                    isClearable
                                    value={modelName}
                                    onChange={handleModelChange}
                                    options={modelOptions}
                                />
                                <Select
                                    placeholder={'Capacity'}
                                    styles={{ menu: ({ ...css }) => ({ ...css, width: 'max-content' }) }}
                                    isClearable
                                    isDisabled={!modelName ? true : false}
                                    value={capacity}
                                    onChange={handleCapacityChange}
                                    options={capacityOptions}
                                />
                                <Select
                                    placeholder={'Color'}
                                    styles={{ menu: ({ ...css }) => ({ ...css, width: 'max-content' }) }}
                                    isClearable
                                    value={color}
                                    isDisabled={!modelName ? true : false}
                                    onChange={handleColorChange}
                                    options={colorOptions}
                                />
                                <button className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow" onClick={handleProductSelect}>
                                    Select
                                </button>
                            </div>
                            <p style={{ color: 'darkred' }}>{notFoundMSG}</p>
                            <div style={{ display: 'flex', flexDirection: 'row' }}>
                                <img src='dummy.png'></img>
                                <div style={{ display: 'flex', flexDirection: 'column' }}>
                                    <span style={{ fontSize: '20px' }}>{userSelectedOption ? userSelectedOption.modelName : ''}</span>
                                    <span>{userSelectedOption ? (userSelectedOption.color ? userSelectedOption.color : '') : ''}</span>
                                    <span>{userSelectedOption ? (userSelectedOption.capacity ? userSelectedOption.capacity : '') : ''}</span>
                                    <span style={{ fontSize: '24px' }}>${Math.round(priceAvg)}</span>
                                </div>


                            </div>
                        </div>

                        <Box minHeight='30vh' style={{ textAlign: '-webkit-center' }}>
                            <LineChart priceData={priceData} priceMin={priceMin} priceMax={priceMax} />
                        </Box >
                    </div>

                    <div style={{ border: '1px solid lightgray', borderRadius: '5px', width: '100%', padding: '10px' }}>
                        <ul>
                            <li style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '10px' }}>
                                <span>Original price</span>
                                <span style={{ backgroundColor: 'lightgray', borderRadius: '3px', padding: '3px 5px' }}>-</span>
                            </li>
                            <li style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '10px' }}>
                                <span>Price decreased</span>
                                <span style={{ backgroundColor: 'lightgray', borderRadius: '3px', padding: '3px 5px' }}>-</span>
                            </li>
                            <li style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '10px' }}>
                                <span>Highest price</span>
                                <span style={{ backgroundColor: 'lightgray', borderRadius: '3px', padding: '3px 5px' }}>{priceMax ? `$` + priceMax : '-'}</span>
                            </li>
                            <li style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingBottom: '10px' }}>
                                <span>Lowest price</span>
                                <span style={{ backgroundColor: 'lightgray', borderRadius: '3px', padding: '3px 5px' }}>{priceMin ? `$` + priceMin : '-'}</span>
                            </li>
                        </ul>
                    </div>


                </div>
                <div>
                    <span style={{ fontSize: '16px', color: '#AD0C0C' }}>Compare with</span>
                    <br />
                    <div style={{ padding: '10px 0', display: 'flex', gap: '10px' }}>
                        <button className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
                            onClick={() => handleManualProductSelect({ model_name: 'iPhone 13', capacity: '128 GB', color: 'MIDNIGHT' })}>
                            iPhone 13 128 GB MIDNIGHT
                        </button>
                        <button className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
                            onClick={() => handleManualProductSelect({ model_name: 'iPhone 14', capacity: '128 GB', color: 'STARLIGHT' })}>
                            iPhone 14 128 GB STARLIGHT
                        </button>

                    </div>

                </div>
            </div>

        </>

    )
}