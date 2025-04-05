import type { ConfigType } from '@plone/registry';

import { socialNetworksSchema } from '../components/Widgets/schema/socialNetworksSchema';

export default function install(config: ConfigType) {
  config.registerUtility({
    name: 'socialNetworks',
    type: 'schema',
    method: socialNetworksSchema,
  });

  return config;
}
