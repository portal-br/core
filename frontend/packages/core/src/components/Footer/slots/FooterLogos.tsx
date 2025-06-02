import { useSelector, shallowEqual } from 'react-redux';
import { useLiveData } from '@kitconcept/volto-light-theme/helpers/useLiveData';
import LogosContainer from '@kitconcept/volto-light-theme/components/LogosContainer/LogosContainer';
import type { Content } from '@plone/types';
import type { SiteFooterSettings } from '@kitconcept/volto-light-theme/types';

type FormState = {
  content: {
    data: Content;
  };
  form: {
    global: Content;
  };
};

const FooterLogos = () => {
  const content = useSelector<FormState, Content>(
    (state) => state.content.data,
    shallowEqual,
  );

  const footer_logos = useLiveData<SiteFooterSettings['footer_logos']>(
    content,
    'portalbrasil.footer',
    'footer_logos',
  );

  const footer_logos_size = useLiveData<
    SiteFooterSettings['footer_logos_size']
  >(content, 'portalbrasil.footer', 'footer_logos_size');
  const footer_logos_container_width = useLiveData<
    SiteFooterSettings['footer_logos_container_width']
  >(content, 'portalbrasil.footer', 'footer_logos_container_width');

  return footer_logos?.length > 0 ? (
    <LogosContainer
      logos={footer_logos}
      logos_size={footer_logos_size}
      logos_container_width={footer_logos_container_width}
    />
  ) : null;
};

export default FooterLogos;
