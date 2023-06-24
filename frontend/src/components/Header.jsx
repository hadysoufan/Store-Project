import React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';

function Header() {
  return (
    <header>
      <Navbar expand="lg" bg="dark" variant="dark" collapseOnSelect>
        <Container fluid>
          <Navbar.Brand href="/">Store Shop</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="mr-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll>
              <Nav.Link href="/cart">
                <i className="fas fa-shopping-cart"></i>Cart
              </Nav.Link>
              <Nav.Link href="/login">
                <i className="fas fa-user"></i>Login
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
