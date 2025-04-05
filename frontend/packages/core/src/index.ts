import type { ConfigType } from '@plone/registry';

import { defineMessages } from 'react-intl';

import installSettings from './config/settings';
import installWidgets from './config/widgets';

defineMessages({
  listWithImages: {
    id: 'List with images',
    defaultMessage: 'List with images',
  },
});

const applyConfig = (config: ConfigType) => {
  installSettings(config);
  installWidgets(config);
  return config;
};

export default applyConfig;
