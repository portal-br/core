import type { ConfigType } from '@plone/registry';

import installSettings from './config/settings';
import installSlots from './config/slots';
import installViews from './config/views';

const applyConfig = (config: ConfigType) => {
  installSettings(config);
  installSlots(config);
  installViews(config);
  return config;
};

export default applyConfig;
