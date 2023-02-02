import React from 'react';
import Navbar from '../components/Navbar';
import GraphLine from '../components/dashboard/GraphLine';
import { Link } from 'react-router-dom';

export default function Dashboard() {
    return (
        <div>
            <Navbar />
            <GraphLine />
        </div>
    )
}