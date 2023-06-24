import React, { useEffect } from 'react';
import { Link, useNavigate, useParams, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {
  Row,
  Col,
  ListGroup,
  Image,
  Form,
  Button,
  Card,
} from 'react-bootstrap';
import { Message } from '../components/Message';
import { addToCart } from '../actions/cartAction';

function Cart() {
  const location = useLocation();
  const navigate = useNavigate();

  const { id } = useParams();

  const qty = location.search ? Number(location.search.split('=')[1]) : 1;

  const dispatch = useDispatch();

  useEffect(() => {
    if (id) {
      dispatch(addToCart(id, qty));
      console.log('added to cart');
    }
  }, [dispatch, id, qty]);

  return <div>caart</div>;
}

export default Cart;
