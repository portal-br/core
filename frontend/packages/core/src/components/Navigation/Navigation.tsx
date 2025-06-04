// SemanticUI-free pre-@plone/components

import React, { useState, useEffect, useRef } from 'react';
import { useDispatch, useSelector, shallowEqual } from 'react-redux';
import { NavLink } from 'react-router-dom';
import doesNodeContainClick from '@kitconcept/volto-light-theme/helpers/doesNodeContainClick';
import { useIntl } from 'react-intl';
import cx from 'classnames';
import { getBaseUrl } from '@plone/volto/helpers/Url/Url';
import { hasApiExpander } from '@plone/volto/helpers/Utils/Utils';
import config from '@plone/volto/registry';

import { getNavigation } from '@plone/volto/actions/navigation/navigation';
import Icon from '@plone/volto/components/theme/Icon/Icon';
import clearSVG from '@plone/volto/icons/clear.svg';
import NavItem from '@plone/volto/components/theme/Navigation/NavItem';
import { useLiveData } from '@kitconcept/volto-light-theme/helpers/useLiveData';
import type { SiteHeaderSettings } from '@kitconcept/volto-light-theme/types';
import type { Content } from '@plone/types';
import messages from '@portalbrasil/core/messages';

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

const Navigation = ({ pathname }) => {
  const [desktopMenuOpen, setDesktopMenuOpen] = useState(null);
  const [currentOpenIndex, setCurrentOpenIndex] = useState(null);
  const navigation = useRef(null);
  const dispatch = useDispatch();
  const intl = useIntl();
  const content = useSelector<FormState, Content>(
    (state) => state.content.data,
    shallowEqual,
  );
  const has_fat_menu = useLiveData<SiteHeaderSettings['has_fat_menu']>(
    content,
    'portalbrasil.header',
    'has_fat_menu',
  );
  const lang = useSelector((state) => state.intl.locale);
  const token = useSelector((state) => state.userSession.token, shallowEqual);
  const items = useSelector((state) => state.navigation.items, shallowEqual);

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (navigation.current && doesNodeContainClick(navigation.current, e))
        return;
      closeMenu(null);
    };

    document.addEventListener('mousedown', handleClickOutside, false);

    return () => {
      document.removeEventListener('mousedown', handleClickOutside, false);
    };
  }, []);

  useEffect(() => {
    if (!hasApiExpander('navigation', getBaseUrl(pathname))) {
      dispatch(getNavigation(getBaseUrl(pathname), config.settings.navDepth));
    }
  }, [pathname, token, dispatch]);

  const isActive = (url) => {
    return (url === '' && pathname === '/') || (url !== '' && pathname === url);
  };

  const openMenu = (index) => {
    if (index === currentOpenIndex) {
      setDesktopMenuOpen(null);
      setCurrentOpenIndex(null);
    } else {
      setDesktopMenuOpen(index);
      setCurrentOpenIndex(index);
    }
  };

  const closeMenu = (index) => {
    setDesktopMenuOpen(null);
    setCurrentOpenIndex(null);
  };

  useEffect(() => {
    const handleEsc = (event) => {
      if (event.keyCode === 27) {
        closeMenu(null);
      }
    };
    window.addEventListener('keydown', handleEsc);

    return () => {
      window.removeEventListener('keydown', handleEsc);
    };
  }, []);

  return (
    <nav
      id="navigation"
      aria-label="navigation"
      className="navigation"
      ref={navigation}
    >
      <div className={'computer large screen widescreen only'}>
        <ul className="desktop-menu">
          {items.map((item, index) => (
            <li key={item.url}>
              {has_fat_menu && item.items?.length > 0 ? (
                <>
                  <button
                    onClick={() => openMenu(index)}
                    className={cx('item', {
                      active:
                        desktopMenuOpen === index ||
                        (!desktopMenuOpen && pathname === item.url),
                    })}
                    aria-label={intl.formatMessage(messages.openFatMenu)}
                    aria-expanded={desktopMenuOpen === index ? true : false}
                  >
                    {item.title}
                  </button>

                  <div className="submenu-wrapper">
                    <div
                      className={cx('submenu', {
                        active: desktopMenuOpen === index,
                      })}
                    >
                      <div className="submenu-inner">
                        <NavLink
                          to={item.url === '' ? '/' : item.url}
                          onClick={() => closeMenu(null)}
                          className="submenu-header"
                        >
                          <h2>{item.nav_title ?? item.title}</h2>
                        </NavLink>
                        <button
                          className="close"
                          onClick={closeMenu}
                          aria-label={intl.formatMessage(messages.closeMenu)}
                        >
                          <Icon name={clearSVG} size="48px" />
                        </button>
                        <ul>
                          {item.items &&
                            item.items.length > 0 &&
                            item.items.map((subitem) => (
                              <li className="subitem-wrapper" key={subitem.url}>
                                <NavLink
                                  to={subitem.url}
                                  onClick={() => closeMenu(null)}
                                  className={cx({
                                    current: isActive(subitem.url),
                                  })}
                                >
                                  <span className="left-arrow">&#8212;</span>
                                  <span>
                                    {subitem.nav_title || subitem.title}
                                  </span>
                                </NavLink>
                                <div className="sub-submenu">
                                  <ul>
                                    {subitem.items &&
                                      subitem.items.length > 0 &&
                                      subitem.items.map((subsubitem) => (
                                        <li
                                          className="subsubitem-wrapper"
                                          key={subsubitem.url}
                                        >
                                          <NavLink
                                            to={subsubitem.url}
                                            onClick={() => closeMenu(null)}
                                            className={cx({
                                              current: isActive(subsubitem.url),
                                            })}
                                          >
                                            <span className="left-arrow">
                                              &#8212;
                                            </span>
                                            <span>
                                              {subsubitem.nav_title ||
                                                subsubitem.title}
                                            </span>
                                          </NavLink>
                                        </li>
                                      ))}
                                  </ul>
                                </div>
                              </li>
                            ))}
                        </ul>
                      </div>
                    </div>
                  </div>
                </>
              ) : (
                <NavItem item={item} lang={lang} key={item.url} />
              )}
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
};

export default Navigation;
