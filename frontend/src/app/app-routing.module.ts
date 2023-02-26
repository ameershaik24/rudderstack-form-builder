import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";

import { SourceComponent } from "./source-data/components/source/source.component";


const routes: Routes = [
  { path: "", redirectTo: "/source", pathMatch: "full" },
  { path: "source", component: SourceComponent, pathMatch: "full" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
