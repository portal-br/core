import type { ConfigType } from '@plone/registry';
import Colophon from '@portalbrasil/core/components/Footer/slots/Colophon';
import FooterLogos from '@portalbrasil/core/components/Footer/slots/FooterLogos';

export default function install(config: ConfigType) {
  config.registerSlotComponent({
    name: 'footerLogos',
    slot: 'preFooter',
    component: FooterLogos,
  });
  config.registerSlotComponent({
    name: 'Colophon',
    slot: 'postFooter',
    component: Colophon,
  });

  return config;
}
