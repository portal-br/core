// SemanticUI-free pre-@plone/components
import { useSelector } from 'react-redux';
import { Container } from '@plone/components';
import MobileNavigation from '@kitconcept/volto-light-theme/components/MobileNavigation/MobileNavigation';
import cx from 'classnames';
import isEmpty from 'lodash/isEmpty';

import LanguageSelector from '@plone/volto/components/theme/LanguageSelector/LanguageSelector';
import Logo from '@plone/volto/components/theme/Logo/Logo';
import Navigation from '@plone/volto/components/theme/Navigation/Navigation';
import SearchWidget from '@plone/volto/components/theme/SearchWidget/SearchWidget';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';

import SlotRenderer from '@plone/volto/components/theme/SlotRenderer/SlotRenderer';

const Header = (props) => {
  const { pathname } = props;
  const content = useSelector((state) => state.content.data);
  const navRoot = useSelector((state) => state.navroot?.data?.navroot);
  const headerSettings = useSelector(
    (state) =>
      state.content.data?.['@components']?.inherit?.['portalbrasil.header']
        ?.data,
  );
  const formData = useSelector((state) => state.form.global);
  const headerActions =
    !isEmpty(formData) && formData?.header_actions
      ? formData.header_actions
      : headerSettings?.header_actions;
  return (
    <>
      <SlotRenderer name="aboveHeader" content={content} navRoot={navRoot} />
      <header className={cx('header-wrapper')}>
        <Container layout>
          <div className="header">
            <div className="tools-wrapper">
              <LanguageSelector />

              <div className="tools">
                {headerActions &&
                  Array.isArray(headerActions) &&
                  headerActions.map((item) => (
                    <UniversalLink
                      key={item['@id']}
                      href={item.href?.[0]['@id']}
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
        </Container>
      </header>
    </>
  );
};

export default Header;
