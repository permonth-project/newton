import React, { useEffect, useState } from "react";
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import axios from "axios";


const GraphBar = () => {
    const [data, setData] = useState();
    const [isFetched, setIsFetched] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                `http://newton.permonth.tech/api/get-avg/?product_id=466`,
            );

            setData(result.data);
            setIsFetched(true)
        };

        fetchData();
    }, []);

    const options = {
        chart: {
            type: 'line'
        },
        title: {
            text: ''
        },
        series: [
            {
                data: data?.map(d => d.price_avg)
            }
        ],

    };

    return (
        <div className='max-w-[1240px] mx-auto px-16 bg-black/0 mt-16 py-8 rounded-xl'>
            <HighchartsReact highcharts={Highcharts} options={options} />
        </div >
    )
}

export default GraphBar;
