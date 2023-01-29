import React from 'react'

const Iphone = () => {
  return (
    <div className='w-full mb-8 sm:px-4 px-2 sm:py-0 py-8' id='faq'>
        <div className='max-w-[1240px] flex flex-col mx-auto bg-black/0 sm:px-16 sm:py-16 border-none rounded-xl '>
        <p className="my-2 text-white font-bold text-sm px-4 py-2 rounded-full w-[240px] text-center bg-[#93123f]/80">
            Do you have any questions?
          </p>
          <h1 className='text-5xl font-bold my-4'>Frequently Asked Question</h1>
        <div className='grid  md:grid-cols-2 gap-8 my-4'>
            <div className='bg-white flex flex-col p-4 rounded-xl hover:scale-105 duration-300'>
            <h3 className='py-2 font-medium text-lg text-gray-800 border-b'>1. How does this help you?</h3>
            <p className='py-2 text-gray-500 '>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem eaque tempore et incidunt officiis voluptas quo id quibusdam ipsam maxime delectus consequuntur dignissimos accusantium voluptate facere, libero aliquid beatae quae.</p>
            </div>


            <div className='bg-white flex flex-col p-4 rounded-xl hover:scale-105 duration-300'>
            <h3 className='py-2 font-medium text-lg text-gray-800 border-b'>2. How does this help you?</h3>
            <p className='py-2 text-gray-500 '>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem eaque tempore et incidunt officiis voluptas quo id quibusdam ipsam maxime delectus consequuntur dignissimos accusantium voluptate facere, libero aliquid beatae quae.</p>
            </div>

        </div>
        <div className='grid  md:grid-cols-2 gap-8 mt-4'>
            <div className='bg-white flex flex-col p-4 rounded-xl hover:scale-105 duration-300'>
            <h3 className='py-2 font-medium text-lg text-gray-800 border-b'>3. How does this help you?</h3>
            <p className='py-2 text-gray-500 '>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem eaque tempore et incidunt officiis voluptas quo id quibusdam ipsam maxime delectus consequuntur dignissimos accusantium voluptate facere, libero aliquid beatae quae.</p>
            </div>


            <div className='bg-white flex flex-col p-4 rounded-xl hover:scale-105 duration-300'>
            <h3 className='py-2 font-medium text-lg text-gray-800 border-b'>4. How does this help you?</h3>
            <p className='py-2 text-gray-500 '>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem eaque tempore et incidunt officiis voluptas quo id quibusdam ipsam maxime delectus consequuntur dignissimos accusantium voluptate facere, libero aliquid beatae quae.</p>
            </div>

        </div>
</div>
    </div>
  )
}

export default Iphone