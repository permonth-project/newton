
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navigate } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';

import Homepage from './pages/Homepage';
import Dashboard from './pages/Dashboard';
import Footer from './components/Footer';


function App() {
  return (
<<<<<<< Updated upstream
    <Router>

      <div className="App">
        <ScrollToTop />
        {/* <Navigate /> */}
        <Routes>
          <Route exact path="/" element={<Homepage />} />
          <Route path="/compare" element={<Dashboard />} />
        </Routes>
        <Footer />
      </div>
    </Router>


=======
    <div className="bg-white">
      <Navbar />
      <Hero />
      <Cards2/>
      <Cards3/>

      <CTA/>
      <Iphone />
      <Footer/>
      
    </div>
>>>>>>> Stashed changes
  );
}

export default App;
