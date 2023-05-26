
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';

import Homepage from './pages/Homepage';
import Dashboard from './pages/Dashboard';
import Footer from './components/Footer';
import ReactDOM from 'react-dom';
import ReactGA from 'react-ga4';
const MEASUREMENT_ID = process.env.REACT_APP_GA_ID
ReactGA.initialize(MEASUREMENT_ID);


function App() {
  useEffect(() => {
    ReactGA.pageview(window.location.pathname + window.location.search);
  }, []);

  return (
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


  );
}

export default App;
