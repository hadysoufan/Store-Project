import React from 'react';
import { Alert } from 'react-bootstrap';

/**
 * Message component for displaying alert messages.
 * @param {Object} props - Component props.
 * @param {string} props.variant - The variant of the alert (e.g., "success", "danger", "warning").
 * @param {ReactNode} props.children - Child components representing the message content.
 */
function Message({ variant, children }) {
  return <Alert variant={variant}>{children}</Alert>;
}

export default Message;
