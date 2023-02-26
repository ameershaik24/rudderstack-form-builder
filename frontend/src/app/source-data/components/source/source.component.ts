import { Component, OnInit } from "@angular/core";
import { NgForm } from "@angular/forms";

import { Source } from "../../interfaces/source";
import { SourceForm } from "../../interfaces/source-form";
import { SourceService } from "../../services/source.service";

@Component({
  selector: 'app-source',
  templateUrl: './source.component.html',
  styleUrls: ['./source.component.scss']
})
export class SourceComponent implements OnInit {

  sourceTypes: { [key: string]: string; } = {};
  sourceForm: SourceForm;

  constructor(private sourceService:SourceService) { }

  ngOnInit() {
    this.getSourceTypes();
  }

  getSourceTypes() {
    this.sourceService.getSourceTypes().subscribe(
      (response) => {
        this.sourceTypes = response;
        console.log("Fetched source types");
      },
      (error) => {
        console.error("Error in getting source types");
      }
    )
  }

  getSourceFormTemplate(sourceType: string) {
    this.sourceService.getSourceFormTemplate(sourceType).subscribe(
      (response) => {
        this.sourceForm = response;
        console.log(`Fetched source form template for ${sourceType}`);
      },
      (error) => {
        console.error("Error in getting source form template");
      }
    )
  }

  createSource(sourceDataForm: NgForm) {
    const sourceDataFormValues = sourceDataForm.value;
    // console.log(sourceDataFormValues);
    // return

    // TODO - fix checkbox value being stored as empty string, if it's untouched

    let sourceData = {};

    sourceData["source_form_template"] = this.sourceForm.id;
    sourceData["company_id"] = 1234;
    sourceData["source_form_data"] = sourceDataFormValues;

    this.sourceService.createSource(sourceData as Source).subscribe(
      (response) => {
        console.info("Successfully saved source data");
      },
      (error) => {
        console.error("Error in saving source form data");
      }
    )
  }

}
