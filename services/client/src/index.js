
import React, { Component } from 'react';    //  new
import ReactDOM from 'react-dom';   // import ReactDom
import axios from 'axios';    // new
import UsersList from './components/UsersList';




class App extends Component {
  constructor() {
    super();
    // new
    this.state = {
      users: []
    };
  };
  // new
  componentDidMount(){
    this.getUsers();
  };
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users }); }) //  new
    .catch((err) => { console.log(err); });
  }
  render() {
    return (
      <section className="section">
        <div className="containers">
          <div className="columns">
            <div className="column is-one-third">
            <br/>
            <h1 className="title is-1">All Users</h1>
            <hr/><br/>
            <UsersList users={this.state.users}/>
          </div>
        </div>
      </div>
    </section>
    )
  }
};


// Use the render method from ReactDOM class to mount the App to the DOM to HTML
// element with an ID of root.
ReactDOM.render(
  <App />,
  document.getElementById('root')
);
