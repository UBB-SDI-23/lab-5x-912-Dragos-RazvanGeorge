
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
//import React from 'react'
import { CarsShowAll } from './components/Cars/CarsShowAll'
import { CarAdd } from './components/Cars/CarsAdd'

import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMenu } from './components/AppMenu'
import { CarDelete } from './components/Cars/CarDelete'
import { CarUpdate } from './components/Cars/CarUpdate'
import { AppHome } from './components/AppHome'
import { CarOwner } from './components/Statistics/CarOwnerReport'

function App() {
  const [count, setCount] = useState(0)

  return (
    <React.Fragment>
      <Router>
        <AppMenu />

        <Routes>
          <Route path="/" element={<AppHome />} />
          <Route path="/cars" element={<CarsShowAll />} />
          <Route path="/cars/add" element={<CarAdd/>}/>
          <Route path="/cars/:carId/delete" element={<CarDelete/>}/>
          <Route path="/cars/:carId/edit" element={<CarUpdate />} />
          <Route path="/car_owner_report" element={<CarOwner/>}></Route>
        </Routes>
      </Router>
    </React.Fragment>
  )
}

export default App
