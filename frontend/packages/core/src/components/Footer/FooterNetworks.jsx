import React from 'react';
import cx from 'classnames';
import { useSelector, shallowEqual } from 'react-redux';
import { getNetworks } from '@plonegovbr/volto-network-block/components/helpers/networks';
import SocialNetworks from '@plonegovbr/volto-network-block/components/SocialNetworks/SocialNetworks';

const convertData = (networks = []) => {
  const ready = networks
    .map((rawItem, idx) => {
      const item = structuredClone(rawItem);
      const { id, href } = item;
      if (href !== undefined) {
        item.url = href['@id'] || href[0]?.['@id'];
        item.icon = id;
        item.id = `network-${id}-${idx}`;
      }
      return item;
    })
    .filter((item) => item.url !== undefined);
  return ready;
};

const FooterLinks = (props) => {
  const animate = props.animate !== undefined ? props.animate : true;
  const align = props.align !== undefined ? props.align : 'left';
  const title = props.title;
  const formState = useSelector((state) => state.form.global);
  const { actionsNetworks = [] } = useSelector(
    (state) => ({
      backendNetworks: state.actions?.actions?.social_actions,
    }),
    shallowEqual,
  );
  const inheritNetworks = useSelector(
    (state) =>
      state.content.data?.['@components']?.inherit?.[
        'portalbrasil.social_networks'
      ]?.data,
  );
  const newStyle = formState?.network_links || inheritNetworks?.network_links;
  const rawNetworks = newStyle ? convertData(newStyle) : actionsNetworks;
  const networks = getNetworks(rawNetworks);
  return (
    networks && (
      <div className={cx('footer_links', align)}>
        {title && <div className="footer_links title">{title}</div>}
        <SocialNetworks networks={networks} animate={animate} align={align} />
      </div>
    )
  );
};

export default FooterLinks;
