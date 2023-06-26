import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

/**
 * Wrapper component for form containers.
 * @param {Object} props - Component props.
 * @param {ReactNode} props.children - Child components.
 */
function FormContainer({ children }) {
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          {children}
        </Col>
      </Row>
    </Container>
  );
}

export default FormContainer;
