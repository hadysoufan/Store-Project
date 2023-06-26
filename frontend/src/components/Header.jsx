import React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

/**
 * Header component representing the navigation bar.
 */
function Header() {
  return (
    <header>
      <Navbar expand="lg" bg="dark" variant="dark" collapseOnSelect>
        <Container fluid>
          {/* Logo */}
          <LinkContainer to="/">
            <Navbar.Brand>Store Shop</Navbar.Brand>
          </LinkContainer>

          {/* Hamburger Menu */}
          <Navbar.Toggle aria-controls="navbarScroll" />

          {/* Navigation Links */}
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="mr-auto my-2 my-lg-0"
              style={{ maxHeight: '100px' }}
              navbarScroll>
              {/* Cart Link */}
              <LinkContainer to="/cart">
                <Nav.Link>
                  <i className="fas fa-shopping-cart"></i>Cart
                </Nav.Link>
              </LinkContainer>

              {/* Login Link */}
              <LinkContainer to="/login">
                <Nav.Link href="/login">
                  <i className="fas fa-user"></i>Login
                </Nav.Link>
              </LinkContainer>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
