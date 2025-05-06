import React from 'react';
import profilePic from './profile.jpg';

function Header() {
  return (
    <div className="bg-primary text-white text-center py-4">
      <img 
        src={profilePic} 
        alt="Ravikanth Reddy" 
        className="rounded-circle" 
        style={{ width: '150px', height: '150px', objectFit: 'cover', border: '4px solid white', marginBottom: '10px' }} 
      />
      <h1>Ravikanth Reddy</h1>
      <p>Software Developer</p>
    </div>
  );
}

export default Header;
