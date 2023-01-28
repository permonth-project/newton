import React from 'react'


const Footer = () => (
    <div className='max-w-[1240px] sm:mb-8 mx-auto sm:py-16 sm:px-16 py-4 px-2 grid md:grid-cols-3 gap-8  bg-[#fff2f1] sm:rounded-3xl'>
        <div>
            <h1 className='w-full text-3xl font-bold text-[#93123f]'>
                NEWTON INDEX
            </h1>
            <p className='py-4'>Newton Index is a platform that provides real-time and historical pricing data for used iPhones.</p>

            <div className='flex flex-col sm:flex-row sm:items-center justify-between w-full'>
            <input className='p-2 flex w-full rounded-md text-black font-medium bg-white' type='email' placeholder='Newsletter'/>
            <button className='bg-[#93123f] text-white rounded-md font-medium w-[200px] sm:ml-4 my-6 px-6 py-2'>Subscribe</button>
  
            </div>
        </div>

        <div className='md:col-span-2 flex justify-between  mt-6 sm:ml-12 sm:px-16 px-4 '>
            <div> 
                <h5 className='font-medium text-gray-400 mb-4'>뭐시꺵이</h5>
                <ul>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                </ul>
            </div>

            <div> 
                <h5 className='font-medium text-gray-400 mb-4'>뭐시꺵이</h5>
                <ul>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                </ul>
            </div>

            <div> 
                <h5 className='font-medium text-gray-400 mb-4'>뭐시꺵이</h5>
                <ul>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                    <li className='py-2 text-sm'>sdfsdf</li>
                </ul>
            </div>
        </div>


    </div>
)

export default Footer