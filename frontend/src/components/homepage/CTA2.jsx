
import React from 'react';
import Roadmap from '../../assets/Roadmap.png';


const CTA2 = () => {
  return (
    <div className='w-full py-8 text-black'>
      <div className='max-w-[1240px] mx-auto grid lg:grid-cols-3  grid-center px-16 py-16  rounded-xl bg-[#fff8f8]'>
        <div className='lg:col-span-1  bg-white rounded-xl p-4 h-fit shadow-md'>
          <h1 className='md:text-4xl sm:text-4xl text-xl font-bold py-2'>Future Roadmap</h1>

          <div className='flex flex-col my-4 py-4 border-b-2 border-red-500'>
            <h2 className='font-bold text-xl text-gray-600 '>Sign up to our newsletter and stay up to date</h2>
            <p>Lorem ipsum dolor sit.</p>
          </div>

          <div className='flex flex-col my-4 py-4 border-b-2 border-red-500'>
            <h2 className='font-bold text-xl text-gray-600 '>Sign up to our newsletter and stay up to date</h2>
            <p>Lorem ipsum dolor sit.</p>
          </div>

          <div className='flex flex-col my-4 py-4'>
            <h2 className='font-bold text-xl text-gray-600 '>Sign up to our newsletter and stay up to date</h2>
            <p>Lorem ipsum dolor sit.</p>
          </div>



        </div>


        <div className=' lg:col-span-2'>
          <img className='mx-auto w-[80%]' src={Roadmap} alt='/' />
        </div>

      </div>
    </div>
  )
}

export default CTA2