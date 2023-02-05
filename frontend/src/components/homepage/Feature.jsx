import React from 'react'

import img1 from '../../assets/NEWTON-FEATURE-1.png';
import img2 from '../../assets/NEWTON-FEATURE-2.png';
import img3 from '../../assets/IMAGE3.png';
import { TbWorldDownload } from 'react-icons/tb';
import { AiOutlineDollarCircle } from 'react-icons/ai';
import { FaChartArea } from 'react-icons/fa';

const Feature = () => {
  return (
    <div className='max-w-[1240px] group mx-auto  px-2 sm:px-0 bg-black/0   mt-4 sm:py-24 py-8 rounded-xl' id='feature'>

   
      
      <h1 className='bg-[#93123f] w-fit mx-auto py-2 px-4 rounded-full font-bold text-center text-white mb-12'>Feature</h1>
      <h1 className='my-8 w-fit mx-auto py-2 px-4 rounded-full font-semibold text-center text-[#1E1E1E] text-4xl font-serif'>Top 3 reasons to use Newton Index</h1>

      


      <div className=' mx-auto md:grid grid-cols-3 gap-8 group-hover '>

        <div className='flex flex-col bg-[#1E1E1E]/0 rounded-lg px-4 py-8 gap-4'>
  <TbWorldDownload size={32}/>
            <h1 className='text-3xl sm:text-xl text-[#93123f] font-bold w-[80%]'>Real-time Price Data Across the Globe 24/7</h1>
          <p className="font-medium text-black/60 text-sm tracking-wide">
            Offers live pricing information for used iPhones, allowing users to stay up-to-date on current market values
          </p>
        </div>

        <div className='flex flex-col bg-[#1E1E1E]/0 rounded-lg px-4 py-8 gap-4'>
  <AiOutlineDollarCircle size={32}/>
            <h1 className='text-3xl sm:text-xl text-[#93123f] font-bold w-[100%]'>Find the Reasonable Price Without Countless Searches</h1>
          <p className="font-medium text-black/60 text-sm tracking-wide">
          Discover fair market value with our pricing tool, which provides users with accurate prices to help users make informed decisions
          </p>
        </div>

        <div className='flex flex-col bg-[#1E1E1E]/0 rounded-lg px-4 py-8 gap-4'>
  <FaChartArea size={32}/>
            <h1 className='text-3xl sm:text-xl text-[#93123f] font-bold w-[100%]'>Interactive Price Chart to Compare and Find Your Price</h1>
          <p className="font-medium text-black/60 text-sm tracking-wide">
          Explore trends with our interactive chart feature, which allows users to visualize historical pricing data
          </p>
        </div>

        {/* <div className='my-8'>
          <h1 className='text-3xl sm:text-2xl text-[#93123f] font-bold'>Find the Reasonable Price</h1>
          <p className="font-medium text-black/60 mt-8  text-base">
            Discover fair market value with our pricing tool, which provides users with accurate prices to help users make informed decisions
          </p>
        </div>
        <div className='my-8'>
          <h1 className='text-3xl sm:text-2xl text-[#93123f] font-bold '>Interactive Price Chart</h1>
          <p className="font-medium text-black/60 mt-8  text-base">
            Explore trends with our interactive chart feature, which allows users to visualize historical pricing data
          </p>
        </div> */}

      </div>




    </div>




  )
}

export default Feature