import type { ConfigType } from '@plone/registry';

// VLibras
import Libras from '@plonegovbr/volto-vlibras/components/Libras';

export default function install(config: ConfigType) {
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

  return config;
}
