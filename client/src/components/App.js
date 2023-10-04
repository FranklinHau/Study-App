//serves as the entry point for my application's frontend
import React from 'react';
import UserComponent from './UserComponent';


function App() {
  return (
    <div className='App'>
      <h1>User Management</h1>
      <UserComponent/>
    </div>
  )
}

export default App;