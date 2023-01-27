import React from 'react'

import img1 from '../assets/NEWTON-FEATURE-1.png';
import img2 from '../assets/NEWTON-FEATURE-2.png';
import img3 from '../assets/IMAGE3.png';

const Cards = () => {
  return (
    <div className='max-w-[1240px] group mx-auto  px-0 bg-black/0   mt-4 py-8 rounded-xl'>

        <div className=' mx-auto md:grid grid-cols-3 gap-8 my-4 group-hover text-center'>
            <div className='my-8'>
            <h1 className='text-2xl text-[#93123f] font-bold'>Real-time Price Data</h1>
            <p className="md:text-lg font-medium text-black/60 mt-8">
            offers live pricing information for used iPhones, allowing users to stay up-to-date on current market values
          </p>
            </div>
            
            <div className='my-8'>
            <h1 className='text-2xl text-[#93123f] font-bold'>Find the Reasonable Price</h1>
            <p className="md:text-lg font-medium text-black/60 mt-8">
            Discover fair market value with our pricing tool, which provides users with accurate prices to help users make informed decisions
          </p>
            </div>
            <div className='my-8'>
            <h1 className='text-2xl text-[#93123f] font-bold '>Interactive Price Chart</h1>
            <p className="md:text-lg font-medium text-black/60 mt-8">
            Explore trends with our interactive chart feature, which allows users to visualize historical pricing data
          </p>
            </div>

        </div>




            </div>

 


  )
}

export default Cards