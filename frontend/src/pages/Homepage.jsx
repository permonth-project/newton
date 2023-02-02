import React from 'react';
import Navbar from '../components/Navbar';
import Hero from '../components/homepage/Hero';
import Cards2 from '../components/homepage/Cards2';
import Cards3 from '../components/homepage/Cards3';
import Iphone from '../components/homepage/Iphone';
import CTA from '../components/homepage/CTA';

export default function Homepage() {
    return (
        <div className="App">
            <Navbar />
            <Hero />
            <Cards2 />
            <Cards3 />
            <CTA />
            <Iphone />
        </div>
    )
}
