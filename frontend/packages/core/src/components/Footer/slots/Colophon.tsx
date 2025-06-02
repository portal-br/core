import { Container } from '@plone/components';
import Copyright from './Copyright';
import Logo from '@kitconcept/volto-light-theme/components/Logo/Logo';
import type { Content } from '@plone/types';
import { useLiveData } from '@kitconcept/volto-light-theme/helpers/useLiveData';
import type { SiteHeaderSettings } from '@kitconcept/volto-light-theme/types';

const Colophon = ({ content }: { content: Content }) => {
  const logo = useLiveData<SiteHeaderSettings['logo']>(
    content,
    'portalbrasil.header',
    'logo',
  );

  return (
    <Container className="colophon">
      <Copyright />
      {!logo && <Logo />}
    </Container>
  );
};

export default Colophon;
