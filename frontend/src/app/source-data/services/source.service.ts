import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

import { environment } from "../../../environments/environment";
import { Source } from "../interfaces/source";
import { SourceForm } from "../interfaces/source-form";

@Injectable({
  providedIn: 'root'
})
export class SourceService {

  private sourceDataAppApiPrefix: string = "source_data";

  private getSourceTypesApiUrl: string = 'get_source_types';
  private getSourceFormTemplateApiUrl: string  = 'source_forms';
  private createSourceApiUrl: string = 'sources';

  constructor(private http: HttpClient) { }

  // GET source types from server
  getSourceTypes(): Observable<any> {
    const apiUrl = `${environment.backendServerUrl}/${this.sourceDataAppApiPrefix}/${this.getSourceTypesApiUrl}`;

    return this.http.get<any>(apiUrl);
  }

  // GET source form template from server
  getSourceFormTemplate(sourceType: string): Observable<SourceForm> {
    const apiUrl = `${environment.backendServerUrl}/${this.sourceDataAppApiPrefix}/${this.getSourceFormTemplateApiUrl}/${sourceType}`;

    return this.http.get<SourceForm>(apiUrl);
  }

  // CREATE source
  createSource(source: Source): Observable<Source> {
    const apiUrl = `${environment.backendServerUrl}/${this.sourceDataAppApiPrefix}/${this.createSourceApiUrl}`;

    return this.http.post<Source>(apiUrl, source);
  }

}
