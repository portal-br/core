import React from 'react';
import { FormattedMessage } from 'react-intl';
import { useSelector, shallowEqual } from 'react-redux';
import { useLocation } from 'react-router-dom';
import Logo from '@plone/volto/components/theme/Logo/Logo';
import { Container } from '@plone/components';
import SlotRenderer from '@plone/volto/components/theme/SlotRenderer/SlotRenderer';
import FooterLinks from './FooterLinks';
import FooterNetworks from './FooterNetworks';

const Footer = () => {
  const { content } = useSelector(
    (state) => ({
      content: state.content.data,
    }),
    shallowEqual,
  );
  const location = useLocation();
  const footerSettings = useSelector(
    (state) =>
      state.content.data?.['@components']?.inherit?.['portalbrasil.footer']
        ?.data,
  );
  const footerLinks = footerSettings?.footer_links;

  return (
    <footer id="footer">
      <SlotRenderer name="preFooter" content={content} location={location} />

      <Container className="footer">
        <FooterLinks links={footerLinks} />
        <FooterNetworks animate={false} align={'left'} />
        <div className="logo">
          <Logo />
        </div>
        <a className="item powered-by" href="https://plone.org">
          <FormattedMessage
            id="Powered by PortalBrasil, Plone & Python"
            defaultMessage="Powered by PortalBrasil, Plone & Python"
          />
        </a>
        <br />
        <div className="footer-branding">
          Made with{' '}
          <span role="img" aria-label="love" style={{ color: 'red' }}>
            ❤️
          </span>{' '}
          by PloneGov-BR
        </div>
      </Container>

      <SlotRenderer name="postFooter" content={content} location={location} />
    </footer>
  );
};

export default Footer;
