import React from 'react';

// Import images from src directly
import driveImg from './destiny.jpeg';
import jobPortalImg from './job.jpg';
import restaurantImg from './restaurant.jpg';
import bridgeImg from './bridge.jpg';

function Projects() {
  const projectList = [
    {
      title: 'Drive to Destiny',
      description: 'A web portal built as part of my diploma and B.Tech final year. I led the development team.',
      image: driveImg
    },
    {
      title: 'Django Job Portal',
      description: 'A full-stack job portal built with Django during my Python full stack training.',
      image: jobPortalImg
    },
    {
      title: 'Restaurant Web Portal',
      description: 'A web application for restaurant listings and ordering, built during my full stack course.',
      image: restaurantImg
    },
    {
      title: 'Bridge Crack Detection Using CNN',
      description: 'Used Convolutional Neural Networks to detect bridge cracks from images. AI-based project.',
      image: bridgeImg
    }
  ];

  return (
    <div className="container my-5">
      <h2 className="text-center mb-4">Projects</h2>
      {projectList.map((project, index) => (
        <div className="card mb-4 shadow" key={index}>
          <div className="row g-0">
            <div className="col-md-4">
              <img 
                src={project.image} 
                alt={project.title} 
                className="img-fluid rounded-start"
                style={{ height: '100%', objectFit: 'cover' }}
              />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h5 className="card-title">{project.title}</h5>
                <p className="card-text">{project.description}</p>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Projects;
