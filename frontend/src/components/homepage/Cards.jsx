import React from 'react'

import img1 from '../../assets/IMAGE1.png';
import img2 from '../../assets/IMAGE2.png';
import img3 from '../../assets/IMAGE3.png';

const Cards = () => {
  return (
    <div className='max-w-[1240px] mx-auto px-16 bg-black/0 mt-16 py-8 rounded-xl'>

      <div className=' mx-auto grid md:grid-cols-2 gap-16 my-4'>
        <div>
          <h1 className='text-5xl font-bold'>Compare & Track</h1>
          <h1 className='text-5xl font-bold'>your iPhone prices</h1>
        </div>
        <div>
          <p className="md:text-1xl text-sm uppercase font-bold text-black/60 mt-8">
            Get the best-in-class group mentoring plans Get the best-in.
          </p>
          <p className="md:text-1xl text-sm uppercase font-bold text-black/60">
            Get the best-in-class group mentoring plans Get the best-in.
          </p>
          <p className="md:text-1xl text-sm uppercase font-bold text-black/60">
            Get the best-in-class group mentoring plans Get the best-in.
          </p>
        </div>

      </div>

      <div className='flex justify-start items-center gap-4 mx-auto mt-16'>
        <a className="relative w-[33%] h-[300px] group rounded-2xl" href="##">
          {/* 이미지 */}
          <img
            className="absolute inset-0 object-cover w-[100%] h-[300px] rounded-2xl group-hover:opacity-90"
            src={img1}
            alt="/" />
          <div className="relative p-5">
            <div className="mt-50">
              <div
                class="transition-all transform 
                                translate-y-1 opacity-0
                                group-hover:opacity-100
                                group-hover:translate-y-0"
              >
                <div className="p-2">
                  <p className="text-3xl font-bold text-[#ffd5e8] mb-4">
                    Real-time price
                  </p>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  </p>
                </div>

              </div>
            </div>
          </div>
        </a>
        <a className="relative w-[33%] h-[300px] group rounded-2xl" href="##">
          {/* 이미지 */}
          <img
            className="absolute inset-0 object-cover w-[100%] h-[300px] rounded-2xl group-hover:opacity-90"
            src={img2}
            alt="/" />
          <div className="relative p-5">
            <div className="mt-50">
              <div
                class="transition-all transform 
                                translate-y-1 opacity-0
                                group-hover:opacity-100
                                group-hover:translate-y-0"
              >
                <div className="p-2">
                  <p className="text-3xl font-bold text-[#ffd5e8] mb-4">
                    Real-time price
                  </p>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  </p>
                </div>

              </div>
            </div>
          </div>
        </a>

        {/* HOVER */}
        <a className="relative w-[33%] h-[300px] group bg-black rounded-2xl" href="##">
          {/* 이미지 */}
          <img
            className="absolute inset-0 object-cover w-[100%] h-[300px] rounded-2xl group-hover:opacity-60"
            src={img3}
            alt="/" />
          <div className="relative p-4">
            <div className="">
              <div
                class="transition-all transform 
                                translate-y-1 opacity-0
                                group-hover:opacity-100
                                group-hover:translate-y-0"
              >
                <div className="p-2">
                  <p className="text-3xl font-bold text-[#ffd5e8] mb-4">
                    Real-time price
                  </p>
                  <ul>
                    <li className='my-2 text-[#ffd5e8] font-medium text-xl'>Lorem ipsum dolor sit amet.</li>
                    <li className='my-2 text-[#ffd5e8] font-medium text-xl'>Lorem ipsum dolor sit amet.</li>
                    <li className='my-2 text-[#ffd5e8] font-medium text-xl'>Lorem ipsum dolor sit amet.</li>
                  </ul>
                  <button className="mt-8 bg-[#ff3b3b] text-Black flex w-[160px] items-center py-2 rounded-md">
                    <span className="mx-auto font-medium text-white text-center">
                      READ MORE
                    </span>
                  </button>
                </div>

              </div>
            </div>
          </div>
        </a>




      </div>

    </div>


  )
}

export default Cards