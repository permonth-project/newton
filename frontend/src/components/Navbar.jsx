import React from 'react';

import logo from '../assets/NEWTON-LOGO.png';

const Navbar = () => {

  return (
    <div className='flex px-2 lg:px-0 justify-between items-center h-24 max-w-[1240px] mx-auto text-black'>
        <img className='w-40' src={logo} alt="/"/>
        <div className='flex items-center'>
        <ul className='hidden lg:flex font-medium'>
            <li className='p-4'>FEATURE</li>
            <li className='p-4'>PROCESS</li>
            <li className='p-4'>ROADMAP</li>
            <li className='p-4'>FAQ</li>
        </ul>
        <button className=" bg-[#93123f] ml-4 text-Black flex w-[160px] items-center py-2 rounded-md">
              <span className="mx-auto font-medium text-white text-center">
                TRY IT
              </span>
            </button>
        </div>
    </div>
  )
}

export default Navbar