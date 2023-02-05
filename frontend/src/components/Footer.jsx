import React from 'react'


const Footer = () => (
    <div className='max-w-[1240px]  mx-auto  grid md:grid-cols-4 px-16 py-16 border-t border-t-[#93123f]'>
        <div className='col-span-1'>
            <h1 className='w-full text-3xl font-bold text-[#93123f]'>
                NEWTON INDEX
            </h1>
            <p className='py-4 text-sm'>Experience the most useful tool for the secondary iphone market price</p>


            <button className='bg-[#93123f] text-white rounded-full font-bold px-8 py-4 text-sm my-2
              hover:text-[#93123f]  hover:border-inside hover:shadow-xl hover:bg-[#93123f]/20
             '>BROWSE</button>
  

        </div>

        <div className='col-span-1'/>

        <div className='md:col-span-2 flex justify-between md:justify-end md:gap-32'>
            <div> 
                <ul>
                <li className='py-2 text-sm font-bold'>Product</li>
                    <li className='py-2 text-sm'>Home</li>
                    <li className='py-2 text-sm'>Feature</li>
                    <li className='py-2 text-sm'>Roadmap</li>
                    <li className='py-2 text-sm'>FAQ</li>
                </ul>
            </div>

            <div> 
                <ul>
                <li className='py-2 text-sm font-bold'>About Us</li>

                    <li className='py-2 text-sm'>Permonth</li>
                    <li className='py-2 text-sm'>Contact Us</li>
                    <li className='py-2 text-sm'>Jiwoo Shim</li>
                    <li className='py-2 text-sm'>Yoon Ro</li>
                </ul>
            </div>

            <div> 
                <ul>
                    <li className='py-2 text-sm font-bold'>Resource</li>
                    <li className='py-2 text-sm'>Process Book</li>
                    <li className='py-2 text-sm'>Blog</li>
                    <li className='py-2 text-sm'>Product</li>
                    <li className='py-2 text-sm'>Privacy</li>
                </ul>
            </div>

            
        </div>

        {/* <div className='py-16 flex justify-between col-span-4 '>
            <p className='text-sm '>Copyright to Permonth </p>
            <div className='flex gap-4'>
                <p>Permonth</p>
                <p>LinkedIn</p>
                <p>LinkedIn</p>
            </div>

 
        </div> */}


    </div>
)

export default Footer