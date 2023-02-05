import React from 'react';
import Navbar from '../components/Navbar';
import Hero from '../components/homepage/Hero';
import Feature from '../components/homepage/Feature';
import Process from '../components/homepage/Process';
import FAQ from '../components/homepage/FAQ';
import Roadmap from '../components/homepage/Roadmap';

export default function Homepage() {
    return (
        <div className="App">
            <Navbar />
            <Hero />
            <Feature />
            <Process />
            <Roadmap />
            <FAQ />
        </div>
    )
}
