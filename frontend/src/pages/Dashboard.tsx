import React from 'react';
import { useAuth } from '../contexts/AuthContext';

const Dashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Dashboard</h1>
      <div style={{
        marginTop: '2rem',
        padding: '1.5rem',
        backgroundColor: '#f5f5f5',
        borderRadius: '8px'
      }}>
        <h2>User Information</h2>
        <p><strong>ID:</strong> {user?.id}</p>
        <p><strong>Email:</strong> {user?.email}</p>
      </div>
      <div style={{
        marginTop: '2rem',
        padding: '1.5rem',
        backgroundColor: '#e8f4f8',
        borderRadius: '8px'
      }}>
        <h3>Welcome to your dashboard!</h3>
        <p>This is a protected route that requires authentication.</p>
        <p>You can add more features and functionality here.</p>
      </div>
    </div>
  );
};

export default Dashboard;
