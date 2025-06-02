import type { ConfigType } from '@plone/registry';

import { defineMessages } from 'react-intl';

import installSettings from './config/settings';
import installSlots from './config/slots';

defineMessages({
  listWithImages: {
    id: 'List with images',
    defaultMessage: 'List with images',
  },
});

const applyConfig = (config: ConfigType) => {
  installSettings(config);
  installSlots(config);
  return config;
};

export default applyConfig;
