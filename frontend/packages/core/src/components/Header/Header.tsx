import React from 'react';
import { useSelector, shallowEqual } from 'react-redux';
import { Container } from '@plone/components';
import cx from 'classnames';

import LanguageSelector from '@plone/volto/components/theme/LanguageSelector/LanguageSelector';
import Logo from '@plone/volto/components/theme/Logo/Logo';
import Navigation from '@plone/volto/components/theme/Navigation/Navigation';
import SearchWidget from '@plone/volto/components/theme/SearchWidget/SearchWidget';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import SlotRenderer from '@plone/volto/components/theme/SlotRenderer/SlotRenderer';

import { useLiveData } from '@kitconcept/volto-light-theme/helpers/useLiveData';

import MobileNavigation from '@kitconcept/volto-light-theme/components/MobileNavigation/MobileNavigation';

import type { SiteHeaderSettings } from '@kitconcept/volto-light-theme/types';
import type { Content } from '@plone/types';

type FormState = {
  content: {
    data: Content;
  };
  navroot: {
    data: {
      navroot: Content;
    };
  };
  form: {
    global: Content;
  };
};

const InternetHeader = ({ pathname, content }) => {
  const header_actions = useLiveData<SiteHeaderSettings['header_actions']>(
    content,
    'portalbrasil.header',
    'header_actions',
  );

  return (
    <>
      <div className="header">
        <div className="tools-wrapper">
          <LanguageSelector />

          <div className="tools">
            {header_actions &&
              Array.isArray(header_actions) &&
              header_actions.map((item) => (
                <UniversalLink
                  key={item['@id']}
                  href={item.href?.[0]['@id']}
                  openLinkInNewTab={item.openInNewTab}
                >
                  {item.title}
                </UniversalLink>
              ))}
          </div>
        </div>
        <div className="logo-nav-wrapper">
          <div className="logo">
            <Logo />
          </div>
          <Navigation pathname={pathname} />
          <MobileNavigation pathname={pathname} />
          <div className="search-wrapper navigation-desktop">
            <div className="search">
              <SearchWidget />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

const Header = (props) => {
  const { pathname } = props;
  const content = useSelector<FormState, Content>(
    (state) => state.content.data,
    shallowEqual,
  );

  const navRoot = useSelector<FormState, Content>(
    (state) => state.navroot?.data?.navroot,
  );

  return (
    <>
      <SlotRenderer name="aboveHeader" content={content} navRoot={navRoot} />
      <header className={cx('header-wrapper')}>
        <Container layout>
          <InternetHeader pathname={pathname} content={content} />
        </Container>
      </header>
      <SlotRenderer name="belowHeader" content={content} navRoot={navRoot} />
    </>
  );
};

export default Header;
