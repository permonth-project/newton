import React from 'react'
import {BsFillPatchQuestionFill} from 'react-icons/bs';

const FAQ = () => {
  return (
    <div className='w-full mb-8 sm:px-4 px-2 sm:py-0 py-8' id='faq'>
        <div className='max-w-[1240px] flex flex-col mx-auto bg-black/0 sm:px-16 sm:py-16 border-none rounded-xl '>
        <p className="my-2 text-white font-bold text-sm px-4 py-2 rounded-full w-[240px] text-center bg-[#93123f]/80">
            Do you have any questions?
          </p>
          <h1 className='text-5xl font-bold my-4'>Frequently Asked Question</h1>
        <div className='grid  md:grid-cols-2 gap-8 my-8'>
            <div className='bg-white flex flex-col rounded-xl'>
            <h3 className='py-2 font-medium text-lg text-gray-800  flex items-center'><BsFillPatchQuestionFill size={20} className='font-bold text-gray-500 mr-2'/>How does&nbsp;<span className='text-[#93123f]'>Newton Index</span>&nbsp;work?</h3>
            <p className='py-2 text-gray-500 text-sm'>We built a data scraping API to collect datas from model, price from high to low, state, storage and colours to provide the interactive chart to users.</p>
            </div>


            <div className='bg-white flex flex-col rounded-xl'>
            <h3 className='py-2 font-medium text-lg text-gray-800  flex items-center'><BsFillPatchQuestionFill size={20} className='text-gray-500 mr-2'/>How does&nbsp;<span className='text-[#93123f]'>support</span>&nbsp;work?</h3>
            <p className='py-2 text-gray-500 text-sm'>Whenever you have feedbacks or problems to share with us, feel free to&nbsp;<span className='text-[#93123f] underline cursor-pointer'>contact us</span>&nbsp;. We are eager to build a great product for users only, so your thought matters to us.</p>
            </div>

        </div>
        <div className='grid  md:grid-cols-2 gap-8 mt-4'>
            <div className='bg-white flex flex-col rounded-xl'>
            <h3 className='py-2 font-medium text-lg text-gray-800  flex items-center'><BsFillPatchQuestionFill size={20} className='text-gray-500 mr-2'/>How can I&nbsp;<span className='text-[#93123f]'>utilize</span>&nbsp;Newton Index?</h3>
            <p className='py-2 text-gray-500 text-sm'>With the pricing tool, users can get a fair and unbiased estimate of the market value of a used iPhone, taking into consideration factors.</p>
            </div>


            <div className='bg-white flex flex-col rounded-xl'>
            <h3 className='py-2 font-medium text-lg text-gray-800  flex items-center'><BsFillPatchQuestionFill size={20} className='text-gray-500 mr-2'/>
            Would there be more products added to the list??            </h3>
            <p className='py-2 text-gray-500 text-sm'>
              Other products like iPads, Macbooks and more will be added in the future. Sign the newsletter for further update!
            </p>
            </div>

        </div>
</div>
    </div>
  )
}

export default FAQ