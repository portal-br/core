/**
 * File view component.
 * @module components/Views/FileView
 */
import React from 'react';
import { Container } from '@plone/components';
import { flattenToAppURL } from '@plone/volto/helpers/Url/Url';
import PDFBlockView from '@eeacms/volto-pdf-block/components/manage/PDFViewer/BlockView';
import FileType from '@kitconcept/volto-light-theme/helpers/Filetype';
import type { Content } from '@plone/types';

interface FileViewProps {
  content: Content;
}

const FileView: React.FC<FileViewProps> = ({ content }) => {
  const contentType = content.file['content-type'];
  const downloadUrl =
    content.file?.download && flattenToAppURL(content.file.download);
  return (
    <Container id="page-document" className="view-wrapper fileitem-view">
      <h1 className="documentFirstHeading">
        {content.title}
        {content.subtitle && ` - ${content.subtitle}`}
      </h1>
      {content.description && (
        <p className="documentDescription">{content.description}</p>
      )}
      {contentType === 'application/pdf' && (
        <PDFBlockView data={{ url: downloadUrl }} />
      )}
      {downloadUrl && (
        <p>
          <a href={downloadUrl}>{content.file.filename}</a>{' '}
          <span>
            ({FileType(content?.file['content-type'])}/{' '}
            {content.file?.size < 1000000
              ? Math.round(content.file.size / 1000)
              : Math.round(content.file.size / 1000000)}
            {content.file?.size < 1000000 ? 'KB' : 'MB'})
          </span>
        </p>
      )}
    </Container>
  );
};

export default FileView;
