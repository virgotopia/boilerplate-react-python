import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const Home: React.FC = () => {
  const { user } = useAuth();

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>FastAPI React Boilerplate</h1>
      <p style={{ fontSize: '1.2rem', marginTop: '1rem' }}>
        A minimal full-stack application with authentication
      </p>
      {!user ? (
        <div style={{ marginTop: '2rem' }}>
          <Link to="/login" style={{
            padding: '0.75rem 1.5rem',
            backgroundColor: '#333',
            color: 'white',
            textDecoration: 'none',
            borderRadius: '4px',
            marginRight: '1rem',
            display: 'inline-block'
          }}>
            Login
          </Link>
          <Link to="/register" style={{
            padding: '0.75rem 1.5rem',
            backgroundColor: '#666',
            color: 'white',
            textDecoration: 'none',
            borderRadius: '4px',
            display: 'inline-block'
          }}>
            Register
          </Link>
        </div>
      ) : (
        <div style={{ marginTop: '2rem' }}>
          <p>Welcome, {user.email}!</p>
          <Link to="/dashboard" style={{
            padding: '0.75rem 1.5rem',
            backgroundColor: '#333',
            color: 'white',
            textDecoration: 'none',
            borderRadius: '4px',
            display: 'inline-block',
            marginTop: '1rem'
          }}>
            Go to Dashboard
          </Link>
        </div>
      )}
    </div>
  );
};

export default Home;
