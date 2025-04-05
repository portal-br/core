import type { ConfigType } from '@plone/registry';

// VLibras
import Libras from '@plonegovbr/volto-vlibras/components/Libras';

export default function install(config: ConfigType) {
  // Idioma em português
  config.settings.defaultLanguage = 'pt-br';
  config.settings.image_crop_aspect_ratios = [
    {
      label: '16:9',
      ratio: 16 / 9,
    },
    {
      label: '4:3',
      ratio: 4 / 3,
    },
    {
      label: '1:1',
      ratio: 1,
    },
  ];

  // Habilita VLibras
  config.settings.appExtras = [
    ...config.settings.appExtras,
    {
      match: '',
      component: Libras,
      props: {},
    },
  ];

  // Expanders
  config.settings.apiExpanders = [
    ...config.settings.apiExpanders,
    {
      match: '',
      GET_CONTENT: ['inherit'],
      querystring: {
        'expand.inherit.behaviors':
          'portalbrasil.header,portalbrasil.footer,portalbrasil.social_networks',
      },
    },
  ];

  return config;
}
