import React from 'react';
import { Link } from 'react-router-dom'
import logo from '../assets/NEWTON-LOGO.png';

const Navbar = () => {

  return (
    <div className='flex px-2 lg:px-0 justify-between items-center h-24 max-w-[1240px] mx-auto text-black'>
      <Link style={{}} to="/">

        <img className='w-40' src={logo} alt="/" />
      </Link>

      <div className='flex items-center'>
        <ul className='hidden lg:flex font-medium'>
          <li className='p-4'><a href='#feature'>FEATURE</a></li>
          <li className='p-4'><a href='#process'>PROCESS</a></li>
          <li className='p-4'><a href='#roadmap'>ROADMAP</a></li>
          <li className='p-4'><a href='#faq'>FAQ</a></li>
        </ul>

        <Link style={{}} to="/compare">
          <button className=" bg-[#93123f] ml-4 text-Black flex w-[160px] items-center py-2 rounded-md">
            <span className="mx-auto font-medium text-white text-center">
              TRY IT
            </span>
          </button>
        </Link>
      </div>
    </div>
  )
}

export default Navbar