import React from 'react'
import logo from '../styles/videohublogo.png'
import videohub from '../styles/Videohub.png'

const Footer = () => {
  return <footer>
    <div className="content">
    <img src={logo} height={100} alt="logo" />
    <p>Lovingly crafted by Raj Bhuva </p>
    <img src={videohub} height={100} alt="videohub" />
    </div>
    <small>Aug 2025</small>
    
  </footer>
}
export default Footer