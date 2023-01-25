import React from 'react'

const Cards3 = () => {
  return (
    <div className='max-w-[1240px] group mx-auto  px-16 bg-[#93123f] text-white mt-16 py-32 sm:rounded-xl'>
        <div className='flex grid md:grid-cols-3 gap-16'>
            <div className=' col-span-1'>
            <h1 className='text-4xl mb-8 font-bold uppercase'>Not sure what good price is?</h1>
            <p>
            If you're unsure of what a fair price is for a used iPhone, Newton Index can help guide you with our pricing tool. When you're looking to purchase a used iPhone or sell your own, our pricing tool can help you navigate the market and find the best deal.
            </p>
            <button className="bg-white text-Black flex w-[160px] items-center py-2 my-8 rounded-md">
              <span className="mx-auto font-medium text-black text-center">
                PROCESS BOOK
              </span>
            </button>
            <p className='text-xs text-white/50'>Read how we come up with the idea and solution.</p>
            </div>
            <div className=' col-span-2'>
            <img className='w-fill rounded-xl'src='https://images.unsplash.com/photo-1605171399454-f2a0e51b811b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1631&q=80' alt='/'/>
            </div>

        </div>
</div>
  )
}

export default Cards3