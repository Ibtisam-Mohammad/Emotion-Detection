import React from 'react';
import './Footer2.css';
import { Link } from 'react-router-dom';

function Footer2() {
  return (
    <div className='footer2-container'>
      <section className='footer2-subscription'>
        {/* <p className='footer2-subscription-heading'>
          Join the Adventure newsletter to receive our best vacation deals
        </p> */}
        {/* <p className='footer2-subscription-text'>
          You can unsubscribe at any time.
        </p> */}
        <div className='input2-areas'>
          {/* <form>
            <input
              className='footer2-input'
              name='email'
              type='email'
              placeholder='Your Email'
            />
            <Button buttonStyle='btn--outline'>Subscribe</Button>
          </form> */}
        </div>
      </section>
      {/* <div class='footer2-links'>
        <div className='footer2-link-wrapper'>
          <div class='footer2-link-items'>
            <h2>About Us</h2>
            <Link to='/sign-up'>How it works</Link>
            <Link to='/'>Testimonials</Link>
            <Link to='/'>Careers</Link>
            <Link to='/'>Investors</Link>
            <Link to='/'>Terms of Service</Link>
          </div>
          <div class='footer2-link-items'>
            <h2>Contact Us</h2>
            <Link to='/'>Contact</Link>
            <Link to='/'>Support</Link>
            <Link to='/'>Destinations</Link>
            <Link to='/'>Sponsorships</Link>
          </div>
        </div>
        <div className='footer2-link-wrapper'>
          <div class='footer2-link-items'>
            <h2>Videos</h2>
            <Link to='/'>Submit Video</Link>
            <Link to='/'>Ambassadors</Link>
            <Link to='/'>Agency</Link>
            <Link to='/'>Influencer</Link>
          </div>
          <div class='footer2-link-items'>
            <h2>social2 Media</h2>
            <Link to='/'>Instagram</Link>
            <Link to='/'>Facebook</Link>
            <Link to='/'>Youtube</Link>
            <Link to='/'>Twitter</Link>
          </div>
        </div>
      </div> */}
      <section class='social2-media'>
        <div class='social2-media-wrap'>
          <div class='footer2-logo'>
            <Link to='/' className='social2-logo'>
              EDAA
              <i class='fab fa-typo3' />
            </Link>
          </div>
          <small class='website2-rights'>EDAA © 2022</small>
          <div class='social2-icons'>
            <Link
              class='social2-icon-link facebook'
              to='/'
              target='_blank'
              aria-label='Github'
            >
              <i class='fa-brands fa-github' />
            </Link>
            <Link
              class='social2-icon-link instagram'
              to='/'
              target='_blank'
              aria-label='Instagram'
            >
              <i class='fab fa-instagram' />
            </Link>
            <Link
              class='social2-icon-link youtube'
              to='/'
              target='_blank'
              aria-label='Youtube'
            >
              <i class='fab fa-youtube' />
            </Link>
            <Link
              class='social2-icon-link twitter'
              to='/'
              target='_blank'
              aria-label='Twitter'
            >
              <i class='fab fa-twitter' />
            </Link>
            <Link
              class='social2-icon-link twitter'
              to='/'
              target='_blank'
              aria-label='LinkedIn'
            >
              <i class='fab fa-linkedin' />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Footer2;