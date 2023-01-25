
import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';

import Cards2 from './components/Cards2';
import Cards3 from './components/Cards3';
import Iphone from './components/Iphone';
import CTA from './components/CTA';
import Footer from './components/Footer';


function App() {
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <Cards2/>
      <Cards3/>

      <CTA/>
      <Iphone />
      <Footer/>
      
    </div>
  );
}

export default App;
