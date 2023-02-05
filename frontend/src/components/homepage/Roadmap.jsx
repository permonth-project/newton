
import React from 'react';
import {RiNumber1} from 'react-icons/ri';

const Roadmap = () => {
  return (
    <div className='w-full text-black' id='roadmap'>
    <div className='max-w-[1240px] mx-auto  px-2 sm:px-16 py-8 sm:py-16 sm:my-8 sm:rounded-xl  '>
      <div className='grid md:grid-cols-4 gap-8'>
        <div className='col-span-2'>
            <h1 className='sm:text-4xl text-5xl font-bold py-2 text-[#93123f]'>Future Roadmap</h1>
            <h1 className='sm:text-4xl text-3xl font-bold py-8'>We have tones of <span className="bg-[#93123f] text-white px-2 italic">features</span> to be updated in the future</h1>

            
        </div>

        
        <div className='max-w-[100%] p-4 rounded-xl bg-[#93123f]/10 col-span-2'>
            <div className='flex flex-col sm:flex-row items-center justify-between w-full'>
            <input className='p-2 flex w-full rounded-md text-black bg-slate-100' type='email' placeholder='Enter Email'/>
            <button className='bg-[#93123f] text-white rounded-md font-medium w-[200px] ml-4 my-6 px-6 py-2'>Notify Me</button>
  
            </div>
            <p className='text-sm'>We care about the protectino of your data. Read our <span className='text-[#93123f] underline'> Privacy Policy.</span></p>
            <p className='text-[#93123f] text-sm'>Sign up to our newsletter and stay up to date</p>
        </div>

        </div>

        <div className=' mx-auto md:grid grid-cols-3  gap-8 mt-16'>

          <div className='rounded-xl p-4  hover:bg-[#ffc9c9] bg-white my-4'>
           <h1 className='text-3xl font-bold text-[#93123f]'>1</h1>
           
           <p className="my-4 md:text-1xl text-sm uppercase font-bold  text-black/60">
            <span className="text-[#93123f] underline">More products will be added</span> into our database including macBook, iMac, iPad and more
          </p>
          </div>

          <div className='rounded-xl p-4  hover:bg-[#ffe7c9] bg-white my-4'>
           <h1 className='text-3xl font-bold text-[#93123f]'>2</h1>
           <p className="my-4 md:text-1xl text-sm uppercase font-bold  text-black/60">
           <span className="text-[#93123f] underline">Buy and sell your products directly</span> from Newton Index. Using unified product template and guide for users
          </p>
          </div>

          <div className='rounded-xl p-4  hover:bg-[#fffdc9] bg-white my-4'>
           <h1 className='text-3xl font-bold text-[#93123f]'>3</h1>
           <p className="my-4 md:text-1xl text-sm uppercase font-bold  text-black/60">
           <span className="text-[#93123f] underline">Data from all over the country</span> will be provided to check your local and global price market
          </p>
          </div>
         

        </div>

    </div>
    </div>
  )
}

export default Roadmap;