import type { BlockEditProps } from '@plone/types';
import { defineMessages } from 'react-intl';
import type { IntlShape } from 'react-intl';

const messages = defineMessages({
  network: {
    id: 'Network',
    defaultMessage: 'Network',
  },
  title: {
    id: 'Title',
    defaultMessage: 'Title',
  },
  item: {
    id: 'Link',
    defaultMessage: 'Link',
  },
  addLink: {
    id: 'Add link',
    defaultMessage: 'Add link',
  },
  Target: {
    id: 'Target',
    defaultMessage: 'Target',
  },
  openLinkInNewTab: {
    id: 'Open in a new tab',
    defaultMessage: 'Open in a new tab',
  },
});

const AvailableNetworks = [
  ['bluesky', 'BlueSky'],
  ['discord', 'Discord'],
  ['docker', 'Docker'],
  ['facebook', 'Facebook'],
  ['flickr', 'Flickr'],
  ['github', 'GitHub'],
  ['gitlab', 'Gitlab'],
  ['instagram', 'Instagram'],
  ['linkedin', 'LinkedIn'],
  ['mastodon', 'Mastodon'],
  ['medium', 'Medium'],
  ['slack', 'Slack'],
  ['soundcloud', 'Soundcloud'],
  ['spotify', 'Spotify'],
  ['stackoverflow', 'StackOverflow'],
  ['telegram', 'Telegram'],
  ['tiktok', 'TikTok'],
  ['twitch', 'Twitch'],
  ['twitter', 'X (Twitter)'],
  ['whatsapp', 'WhatsApp'],
  ['xing', 'Xing'],
  ['youtube', 'YouTube'],
];

export function socialNetworksSchema({
  props,
  intl,
}: {
  props: BlockEditProps;
  intl: IntlShape;
}) {
  return {
    title: intl.formatMessage(messages.item),
    addMessage: intl.formatMessage(messages.addLink),
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['id', 'title', 'href'],
      },
    ],

    properties: {
      id: {
        title: intl.formatMessage(messages.network),
        choices: AvailableNetworks,
        noValueOption: false,
      },
      title: {
        title: intl.formatMessage(messages.title),
      },
      href: {
        title: intl.formatMessage(messages.Target),
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description', '@type'],
        allowExternals: true,
      },
    },
    required: [],
  };
}
