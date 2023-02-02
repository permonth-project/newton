import React from 'react'


const Footer = () => (
    <div className='max-w-[1240px] sm:mb-8 mx-auto sm:py-8 sm:px-16 py-4 px-2 grid md:grid-cols-3 gap-8  bg-[#fff2f1] sm:rounded-3xl'>
        <div>
            <h1 className='w-full text-3xl font-bold text-[#93123f]'>
                NEWTON INDEX
            </h1>
            <p className='py-4 text-sm'>Newton Index is a platform that provides real-time and historical pricing data for used iPhones.</p>

            <div className='flex flex-col sm:flex-row sm:items-center justify-between w-full'>
            <input className='p-2 flex w-full rounded-md text-black font-medium bg-white' type='email' placeholder='Newsletter'/>
            <button className='bg-[#93123f] text-white rounded-md font-medium w-[200px] sm:ml-4 my-6 px-6 py-2'>Subscribe</button>
  
            </div>
        </div>

        <div className='md:col-span-2 flex justify-between md:justify-evenly  sm:ml-8  px-4 items-center'>
            <div> 
                <h5 className='font-bold text-lg text-[#93123f] mb-4 '>Product</h5>
                <ul>
                    <li className='py-2 text-sm'>Home</li>
                    <li className='py-2 text-sm'>Feature</li>
                    <li className='py-2 text-sm'>Roadmap</li>
                    <li className='py-2 text-sm'>Faq</li>
                </ul>
            </div>

            <div> 
            <h5 className='font-bold text-lg text-[#93123f] mb-4'>About Us</h5>
                <ul>
                    <li className='py-2 text-sm'>Permonth</li>
                    <li className='py-2 text-sm'>Contact Us</li>
                    <li className='py-2 text-sm'>Jiwoo Shim</li>
                    <li className='py-2 text-sm'>Yoon Ro</li>
                </ul>
            </div>

            <div> 
            <h5 className='font-bold text-lg text-[#93123f] mb-4'>Resources</h5>
                <ul>
                    <li className='py-2 text-sm'>Process Book</li>
                    <li className='py-2 text-sm'>Blog</li>
                    <li className='py-2 text-sm'>Product</li>
                    <li className='py-2 text-sm'>Privacy</li>
                </ul>
            </div>

            
        </div>


    </div>
)

export default Footer