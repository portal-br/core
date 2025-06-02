import { FormattedMessage } from 'react-intl';
import { Container } from '@plone/components';

const Copyright = () => {
  return (
    <Container className="default copyright">
      <div className="footer-message">
        <a className="item powered-by" href="https://plone.org">
          <FormattedMessage
            id="Criado com PortalBrasil, Plone & Python"
            defaultMessage="Criado com PortalBrasil, Plone & Python"
          />
        </a>
        <br />
        <div className="footer-branding">
          <FormattedMessage
            id="O PortalBrasil é mantido pela comunidade"
            defaultMessage="O PortalBrasil é mantido pela comunidade"
          />{' '}
          <a className="item powered-by" href="https://plone.org.br">
            PloneGov-BR
          </a>
        </div>
      </div>
    </Container>
  );
};

export default Copyright;
